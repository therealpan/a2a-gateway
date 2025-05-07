#!/bin/bash

echo "🔧 Installing dependencies..."
pip install -e .[dev]

echo "✅ Running tests..."
pytest

echo "📦 Building distribution..."
python -m build

echo "🚀 Ready to publish with: twine upload dist/*"
