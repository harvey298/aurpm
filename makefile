build:
	@cargo build --release
	@echo "The files you need can be found at target/release"

clean:
	@cargo clean

install:
	@cargo build --release
	sudo cp target/release /usr/bin/aurpm
	@echo "aurpm is now installed on your system!"