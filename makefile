build:
	@cargo build --release
	@echo "The files you need can be found at target/release"

clean:
	@cargo clean