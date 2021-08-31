main:
	pyinstaller --clean --specpath build/specs -n aurpm -F src/main.py
clean:
	rm -r dist
	rm -r build
	rm -r src/__pycache__/
	rm *.spec

install:
	pyinstaller --clean --specpath build/specs -n aurpm -F src/main.py
	sudo cp dist/aurpm /usr/bin/