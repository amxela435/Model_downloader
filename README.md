# Download model from HF

## how to Run on Linux

1. Run bin
./download_model_HF.bin
* Running on local URL:  http://127.0.0.1:7861
* To create a public link, set `share=True` in `launch()`.

2. In Browser 
http://127.0.0.1:7861/

3. In GUI
- Repo ID e.g. microsoft/Phi-3-mini-4k-instruct-gguf, then press Scan Repo 
- Select needed quantization, e.g. Phi-3-mini-4k-instruct-q4.gguf
- Select local folder, e.g ./models/phi3
- press "Download selected file"

WARNING: can take a long time.
Check your terminal/console window to see the download progress bar.

Tested on Ubuntu 24.04
