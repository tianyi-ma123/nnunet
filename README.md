

1. Get `data`


2. Install `Torch` for CUDA `12.9`

```sh
python -m pip install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu129
```

3. Clone nnUNet

```sh
git clone https://github.com/MIC-DKFZ/nnUNet.git
cd nnUNet
python -m pip install -e .
```

4. Fix nnUNet

In `nnuNet/nnunetv2/experiment_planning/verify_dataset_integrity.py`

ensure that found_labels are list of `np.int64`

```py
def verify_labels(label_file: str, readerclass: Type[BaseReaderWriter], expected_labels: List[int]) -> bool:
    rw = readerclass()
    seg, properties = rw.read_seg(label_file)
    found_labels = np.sort(pd.unique(seg.ravel()))  # np.unique(seg)
    found_labels = [np.int64(i) for i in found_labels] # fix
    ...
```

5. Follow [tutorial](https://pycad.co/nnunet-for-medical-image-segmentation/)