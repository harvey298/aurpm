pub mod termUtil {
    pub fn term_Out(message: &str) {
        let prefix: &str = "[main]";
        println!("{}: {}",prefix, message);
    }
    pub fn term_Out_Err(message: &str) {
        let prefix: &str = "[ERROR]";
        println!("{}: {}",prefix, message);

    }
}