pub mod repoManage {
  pub fn repoAdd() {
    // Repo Command:
   
    // Todo: Add aurpm config reader
        match env::var(key) {
            Ok(val) => {
                let working_dir_tmp: String = val + &"/.aurpm/repo/".to_string()+"aurpm.db.tar.xz".to_string();
                let working_dir_str: &str = &working_dir_tmp[..];
                let working_dir = Path::new(working_dir_str);
                if working_dir.exists() == false {
                    Command::new("mkdir").arg("-p").arg(working_dir_str).spawn().expect("Failed to run command!").wait().unwrap();
                } // Start Repo 
                  // repo-add -n -R $HOME/.aurpm/repo/aurpm.db.tar.xz work/*/*.pkg.tar.zst
                  Command::new("repo-add").arg("-n").arg("-R").arg(working_dir_str).arg("work/*/*.pkg.tar.zst").spawn().expect("Failed to run cmd").wait().unwrap();
                  println!("Finished Repo");

            }, 
            Err(e) => println!("couldn't interpret {}: {}", key, e),
        }
  }
}
