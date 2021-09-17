pub mod pkgmanagement {
    use std::{env, process::{Child, Command}};
    use std::path::Path;

    pub fn build(pkg_name: String) {
        let key = "HOME";
        let pkg_url_tmp: String = "https://aur.archlinux.org/".to_string() + &pkg_name;
        let pkg_url: &str = &pkg_url_tmp[..];
        match env::var(key) {
            Ok(val) => {
                let working_dir_tmp: String = val + &"/.aurpm/work/".to_string();
                let working_dir_str: &str = &working_dir_tmp[..];
                let working_dir = Path::new(working_dir_str);
                if working_dir.exists() == false {
                    Command::new("mkdir").arg("-p").arg(working_dir_str).spawn().expect("Failed to run command!").wait().unwrap();
                }
                let mut git_clone = Command::new("git").current_dir(working_dir_str).arg("clone").arg(pkg_url).spawn().expect("failed to execute process");
                git_clone.wait().unwrap();
                println!("Building!");
                let pkg_work_dir = working_dir_tmp + &pkg_name;
                let mut makepkg_cmd: Child = Command::new("makepkg").current_dir(pkg_work_dir).arg("-sic").spawn().expect("failed to execute process");
                makepkg_cmd.wait().unwrap();
                println!("Package installed!");

            }, 
            Err(e) => println!("couldn't interpret {}: {}", key, e),
        }
        
    }

    pub fn update(pkg_dir: &str) {
        
    }
    
}
