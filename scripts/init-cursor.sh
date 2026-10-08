#!/bin/bash

SRC_DIR="$HOME/.agents/rules"
DEST_DIR="$PWD/.cursor/rules"

mkdir -p "$DEST_DIR"

ln -sf "$SRC_DIR/enforce-clarity.md" "$DEST_DIR/enforce-clarity.mdc"
ln -sf "$SRC_DIR/no-guessing.md" "$DEST_DIR/no-guessing.mdc"
ln -sf "$SRC_DIR/writing-style.md" "$DEST_DIR/writing-style.mdc"
