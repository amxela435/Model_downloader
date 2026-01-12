import os
import gradio as gr
from huggingface_hub import hf_hub_download, list_repo_files

def get_file_list(hf_repo):
    """Fetches all .gguf files from the repository."""
    hf_repo = hf_repo.strip()
    if not hf_repo:
        return gr.update(choices=[], value=None), "❌ Enter a repo path first."
    
    try:
        files = list_repo_files(repo_id=hf_repo)
        gguf_files = [f for f in files if f.lower().endswith(".gguf")]
        
        if not gguf_files:
            return gr.update(choices=[], value=None), "ℹ️ No GGUF files found in this repo."
        
        gguf_files.sort()
        return gr.update(choices=gguf_files, value=gguf_files[0]), "✅ Files fetched! Select one below."
    except Exception as e:
        return gr.update(choices=[], value=None), f"❌ Error fetching files: {e}"

def download_selected_file(hf_repo, local_dir, file_name):
    """Downloads the file with progress shown in the Terminal."""
    hf_repo = hf_repo.strip()
    local_dir = local_dir.strip()

    if not hf_repo or not local_dir or not file_name:
        return "❌ Missing Information. Ensure Repo, Folder, and File are selected."

    try:
        os.makedirs(local_dir, exist_ok=True)
        
        # Download logic - progress will appear in your terminal/console
        print(f"\n--- Starting Download: {file_name} ---")
        file_path = hf_hub_download(
            repo_id=hf_repo,
            filename=file_name,
            local_dir=local_dir
        )
        print(f"--- Finished: {file_path} ---\n")

        return f"✅ Done! Check your terminal for progress details.\nSaved to: {file_path}"
    
    except Exception as e:
        return f"❌ Download Error: {e}"

with gr.Blocks() as demo:
    gr.Markdown("# 📥 Selective GGUF Downloader")
    gr.Markdown("ℹ️ *Check your terminal/console window to see the download progress bar.*")
    
    with gr.Row():
        hf_repo = gr.Textbox(
            label="Hugging Face Repo",
            value="microsoft/Phi-3-mini-4k-instruct-gguf",
            scale=2
        )
        fetch_btn = gr.Button("🔍 Scan Repo", scale=1)

    file_dropdown = gr.Dropdown(
        label="Select Specific Quantization (.gguf)",
        choices=[],
        interactive=True
    )

    local_dir = gr.Textbox(
        label="Local Storage Folder",
        value="./models/phi3"
    )

    status = gr.Textbox(label="Status/Log", interactive=False, lines=3)
    download_btn = gr.Button("🚀 Download Selected File", variant="primary")

    # Event Listeners
    fetch_btn.click(
        get_file_list, 
        inputs=[hf_repo], 
        outputs=[file_dropdown, status]
    )
    
    download_btn.click(
        download_selected_file, 
        inputs=[hf_repo, local_dir, file_dropdown], 
        outputs=status
    )

if __name__ == "__main__":
    # Launching with a soft theme via the proper 6.0 method
    # demo.launch(theme=gr.themes.Soft())
    demo.launch(theme=gr.themes.Monochrome())