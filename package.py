"""
Packages the extension into a clean ZIP archive ready for Chrome Web Store upload.
"""
import json
import os
import zipfile

def package_extension():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    manifest_path = os.path.join(root_dir, 'manifest.json')

    with open(manifest_path, 'r', encoding='utf-8') as f:
        manifest = json.load(f)

    version = manifest.get('version', '1.0.0')
    zip_filename = f'yes-or-no-v{version}.zip'
    zip_path = os.path.join(root_dir, zip_filename)

    # Core production files to include in extension package
    include_files = [
        'manifest.json',
        'popup.html',
        'popup.css',
        'popup.js',
    ]

    include_dirs = [
        'icons'
    ]

    print(f'Creating Chrome Web Store package: {zip_filename}...')
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        for file_name in include_files:
            file_path = os.path.join(root_dir, file_name)
            if os.path.exists(file_path):
                zf.write(file_path, arcname=file_name)
                print(f'  + {file_name}')
            else:
                print(f'  ! Missing: {file_name}')

        for dir_name in include_dirs:
            dir_path = os.path.join(root_dir, dir_name)
            if os.path.exists(dir_path):
                for sub_file in os.listdir(dir_path):
                    sub_path = os.path.join(dir_path, sub_file)
                    if os.path.isfile(sub_path):
                        arcname = f'{dir_name}/{sub_file}'
                        zf.write(sub_path, arcname=arcname)
                        print(f'  + {arcname}')

    size_kb = os.path.getsize(zip_path) / 1024
    print(f'\nSuccess! Package ready at: {zip_filename} ({size_kb:.1f} KB)')

if __name__ == '__main__':
    package_extension()
