main:
	pyinstaller --clean -F index.py

setup:
	pyinstaller --clean -F setup.py

clean:
	rm -r dist
	rm -r build
	rm -r __pycache__/
	rm *.spec