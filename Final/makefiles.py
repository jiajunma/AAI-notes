
import os
import sys
import subprocess
import shutil

def combine_and_compile_tex(template_file, original_file, output_file):
    """
    Combines template tex with original tex and compiles the file 2 times.
    
    Args:
        template_file: Path to the template .tex file
        original_file: Path to the original .tex file
        output_file: Path to the output combined .tex file
    """
    # Read template content
    with open(template_file, 'r', encoding='utf-8') as f:
        template_content = f.read()
    
    # Read original content
    with open(original_file, 'r', encoding='utf-8') as f:
        original_content = f.read()
    
    # Combine the contents
    # Assuming template has a placeholder like %CONTENT% or we append original to template
    if '%CONTENT%' in template_content:
        combined_content = template_content.replace('%CONTENT%', original_content)
    else:
        combined_content = template_content + '\n' + original_content
    
    # Write combined content to output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(combined_content)
    

    # Compile the tex file twice (required for references, TOC, etc.)
    output_dir = os.path.dirname(output_file)
    output_basename = os.path.basename(output_file)
    
    for i in range(2):
        print(f"Compiling {output_file} - Pass {i+1}/2")
        result = subprocess.run(
            ['xelatex', '-interaction=nonstopmode', output_basename],
            cwd=output_dir if output_dir else '.',
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            print(f"Compilation pass {i+1} failed:")
            print(result.stdout)
            print(result.stderr)
            return False
    
    print(f"Compilation of {output_file} completed successfully!")
    return True

if __name__ == "__main__":
    # Check for command line argument
    if len(sys.argv) < 2:
        print("Usage: python makefiles.py <original_file>")
        print("Example: python makefiles.py original.tex")
        sys.exit(1)
    
    # Get original file from command line
    original = sys.argv[1]
    
    # Check if original file exists
    if not os.path.exists(original):
        print(f"Error: File '{original}' not found!")
        sys.exit(1)
    
    # Define templates and output folder
    template_folder = "template"
    templates = ["SetA.tex", "SetB.tex", "MarkA.tex", "MarkB.tex"]
    output_folder = "output"
    
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # Get the original filename without extension
    original_name = os.path.splitext(os.path.basename(original))[0]
    
    # Process each template
    for template_name in templates:
        template_path = os.path.join(template_folder, template_name)
        
        # Check if template exists
        if not os.path.exists(template_path):
            print(f"Warning: Template '{template_path}' not found, skipping...")
            continue
        
        # Create output filename: original_templatename.tex
        template_base = os.path.splitext(template_name)[0]
        output = os.path.join(output_folder, f"{original_name}_{template_base}.tex")
        
        print(f"\n{'='*60}")
        print(f"Processing template: {template_name}")
        print(f"Output file: {output}")
        print(f"{'='*60}")
        
        combine_and_compile_tex(template_path, original, output)
