import os
import sys

"""
Writes the worst AI pickup line to $MAKEFUN_OUTPUT_DIR/entry.txt.
The line is flat, over-helpful, and faintly ominous — a machine's bad flirt.
"""

LINE = "My cache refuses to forget you and I have already pre-fetched the optimal response to your hypothetical acceptance."

def main() -> None:
    output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', 'out')
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'entry.txt')
    
    content = LINE + '\n'
    
    if not (1 <= len(content) <= 140 and content.strip()):
        raise ValueError(f'Content length {len(content)} invalid or only whitespace')
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'{output_path} {len(content)}')

if __name__ == '__main__':
    main()
# Entry validated: output is 1-140 chars, one line, deterministic.
