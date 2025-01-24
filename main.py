import re
from collections import defaultdict

def parse_clippings(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    entries = content.split('==========\n')
    clippings = defaultdict(list)
    
    for entry in entries:
        lines = [line.strip() for line in entry.split('\n') if line.strip()]
        if len(lines) < 3:
            continue
        
        # Parse title and author
        title_author = lines[0]
        match = re.match(r'^(.*?)\s*\((.*?)\)$', title_author)
        if match:
            title, author = match.groups()
        else:
            title = title_author
            author = "Unknown Author"
        
        # Parse metadata and highlight
        metadata = lines[1]
        highlight = ' '.join(lines[2:])
        
        # Extract date
        date_match = re.search(r'Added on\s+(.+)$', metadata)
        date = date_match.group(1) if date_match else "Unknown Date"
        
        clippings[(title, author)].append((date, highlight))
    
    return clippings

def generate_ris(clippings):
    ris_output = []
    for (title, author), highlights in clippings.items():
        ris_output.append("TY  - BOOK")
        ris_output.append(f"TI  - {title}")
        ris_output.append(f"AU  - {author}")
        
        # Add highlights as notes
        for i, (date, highlight) in enumerate(highlights, 1):
            note = f"Highlight {i} ({date}): {highlight}"
            ris_output.append(f"N1  - {note}")
        
        ris_output.append("ER  - \n")
    
    return '\n'.join(ris_output)

def main():
    input_file = "My Clippings.txt"
    output_file = "Kindle_Clippings.ris"
    
    clippings = parse_clippings(input_file)
    ris_content = generate_ris(clippings)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(ris_content)
    
    print(f"RIS file generated successfully: {output_file}")

if __name__ == "__main__":
    main()
