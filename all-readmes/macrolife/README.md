# Macrolife

Macrolife is a small, reproducible image-processing environment built around a curated image collection and a minimal set of general-purpose image and media tools.

The repository contains the image assets and the complete Docker build pipeline. A prebuilt container is also published on Docker Hub for use without a local build.

![](demo.png)

## Docker

The prebuilt Macrolife image is available on Docker Hub:

https://hub.docker.com/r/mechachleopteryx/macrolife

Pull the latest image:

```bash
docker pull mechachleopteryx/macrolife:latest
```

Run it interactively:

```bash
docker run --rm -it mechachleopteryx/macrolife:latest
```

Inside the container, the Macrolife image collection is available at:

```text
/macrolife/images
```

The default working directory is:

```text
/macrolife
```

## Included Tools

The container provides a compact collection of general-purpose image and media-processing tools.

**ImageMagick** provides image conversion, resizing, compositing, filtering, and inspection. **libvips** provides fast, memory-efficient image processing. **FFmpeg** provides image-sequence, video, audio, codec, filtering, and format-conversion facilities. **Python 3** provides a general scripting environment for constructing higher-level processing pipelines.

The intention is to keep the base environment relatively small rather than preinstalling a large collection of specialized packages.

## Images

The repository contains the working Macrolife image collection under:

```text
images/
```

These images are reduced-resolution versions of the original source material. The reduction keeps the repository practical to clone while preserving a directly usable collection rather than packaging the assets inside an opaque archive.

The full-resolution source images are maintained separately under:

```text
source-images/
```

`source-images/` is intentionally excluded from Git.

The repository versions were produced by reducing both dimensions of the source PNG images by 50%. This results in approximately one quarter of the original pixel count.

For example:

```bash
mkdir -p images

for f in source-images/*.png; do
    magick "$f" -resize 50% "images/$(basename "$f")"
done
```

The resulting collection is approximately 123 MB, compared with roughly 500 MB for the full-resolution source set.

## Building Macrolife

Clone the repository and build the container from its root:

```bash
docker build -t mechachleopteryx/macrolife:latest .
```

Run the locally built image:

```bash
docker run --rm -it mechachleopteryx/macrolife:latest
```

The Dockerfile copies the repository's `images/` directory into the resulting container, so the built image is self-contained.

## Testing the Environment

Once inside the container, the installed tools can be checked with:

```bash
magick --version
ffmpeg -version
vips --version
python3 --version
```

Inspect the bundled image collection with:

```bash
ls -lh /macrolife/images
```

A simple ImageMagick test can be performed without modifying the bundled collection:

```bash
mkdir -p /tmp/macrolife-test

f=$(find /macrolife/images -type f -iname '*.png' | head -1)

magick "$f" -resize 25% /tmp/macrolife-test/output.png

identify "$f" /tmp/macrolife-test/output.png
```

## Using Host Files

The bundled collection is useful for experimentation, but Macrolife can also process files from the host by mounting a directory into the container:

```bash
docker run --rm -it \
    -v "$PWD:/work" \
    mechachleopteryx/macrolife:latest
```

The host directory will then be available inside the container at:

```text
/work
```

This allows Macrolife to operate as a disposable image-processing environment without copying additional files into the container itself.

## Publishing

The Docker image is tagged under:

```text
mechachleopteryx/macrolife
```

A local build can be pushed to Docker Hub with:

```bash
docker push mechachleopteryx/macrolife:latest
```

Versioned releases can be tagged independently:

```bash
docker tag mechachleopteryx/macrolife:latest \
    mechachleopteryx/macrolife:v0.1

docker push mechachleopteryx/macrolife:v0.1
```

This allows `latest` to follow current development while preserving named versions of the environment.

## Repository Structure

```text
macrolife/
├── Dockerfile
├── .dockerignore
├── .gitignore
├── README.md
├── workflow.json
├── images/
└── source-images/     # local full-resolution sources; ignored by Git
```

The distinction between `images/` and `source-images/` is intentional. Git contains the practical distribution set, while the larger source collection remains outside repository history.

Likewise, `.dockerignore` prevents the full-resolution sources from being unnecessarily transferred into the Docker build context.

## Image Generation Provenance

The image collection predates the minimal Macrolife processing container. The images were generated with a Stable Diffusion pipeline whose workflow is preserved in:

```text
workflow.json
```

`workflow.json` is included in the repository so that the generation pipeline itself remains inspectable rather than being represented only by a prose description.

The generation pipeline used the Stable Diffusion 1.5 checkpoint:

```text
v1-5-pruned-emaonly.ckpt
```

The checkpoint itself is not included in this repository.

The Stable Diffusion runtime environment used for generation was based on:

https://github.com/AbdBarho/stable-diffusion-webui-docker

That project provides a Docker-based environment for running Stable Diffusion with user-facing interfaces and supporting runtime configuration.

The broad provenance chain is therefore:

```text
workflow.json
        |
        v
v1-5-pruned-emaonly.ckpt
        |
        v
AbdBarho/stable-diffusion-webui-docker
        |
        v
generated full-resolution images
        |
        v
source-images/
        |
        |  ImageMagick: -resize 50%
        v
images/
        |
        v
Macrolife Docker image
```

The full-resolution generated outputs are retained locally as `source-images/` but are excluded from Git because of their substantially larger size. The reduced-resolution `images/` collection is the distribution set tracked by the repository and incorporated into the Macrolife container.

## Checkpoint Identification

For stronger reproducibility, a local copy of the checkpoint can be identified by its SHA-256 digest rather than relying solely on its filename.

On a system containing the checkpoint, run:

```bash
sha256sum v1-5-pruned-emaonly.ckpt
```

The resulting digest can be recorded alongside the checkpoint name:

```text
Checkpoint: v1-5-pruned-emaonly.ckpt
SHA-256: <hash>
```

This is useful because filenames are descriptive rather than cryptographic identifiers. Recording the digest establishes precisely which checkpoint file was used without requiring the multi-gigabyte model itself to be stored in this repository.

## Reproducibility

Macrolife separates three related but distinct artifacts.

The **generation workflow** is preserved as `workflow.json`. The **generated image collection** is preserved in repository-friendly form under `images/`. The **processing environment** is specified by the Dockerfile and distributed as a prebuilt Docker image.

The model checkpoint is treated as an external dependency and identified by name, with provision for recording its cryptographic digest.

This separation means that the repository does not need to contain every byte involved in the original generation process in order to preserve a useful account of how the collection was produced.

## Philosophy

Macrolife treats the container as a reproducible processing environment rather than as a manually prepared machine.

The Dockerfile is therefore the authoritative description of the current environment. The container can be discarded and rebuilt from the repository at any time.

The project deliberately begins with a small set of broadly capable tools. Additional dependencies can be introduced when a concrete processing task requires them rather than accumulating packages speculatively.

The result is intended to remain understandable, rebuildable, and useful both as a standalone image-processing environment and as a foundation for later Macrolife experiments.

