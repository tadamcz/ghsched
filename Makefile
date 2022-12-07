all: generate

generate:
	@echo "Generating files..."
	python make/make.py

clean:
	@echo "Deleting all files in .github/workflows..."
	rm -rf .github/workflows