pub mod repoManage {
  use std::fs;
  pub fn repoAddMass() {
   
    // Todo: Add aurpm config reader
        match env::var(key) -> std::io::Result<()> {
            Ok(val) => {
                let repo_dir_tmp: String = val + &"/.aurpm/repo/".to_string()+"aurpm.db.tar.xz".to_string();
                let working_repo_dir_str: &str = repo_dir_tmp[..];
                let repo_dir = Path::new(working_repo_dir_str);
                if repo_dir.exists() == false {
                    Command::new("mkdir").arg("-p").arg(working_repo_dir_str).spawn().expect("Failed to run command!").wait().unwrap();
                } // Start Repo 
                  // repo-add -n -R $HOME/.aurpm/repo/aurpm.db.tar.xz work/*/*.pkg.tar.zst
                  Command::new("repo-add").arg("-n").arg("-R").arg(working_repo_dir_str).arg("work/*/*.pkg.tar.zst").spawn().expect("Failed to run cmd").wait().unwrap();
                  // Something I found when using aurpm-repo (Python Version) was that it wanted the packages in the same folder as the repo, this attempts to solve the issue
                  // Is Untested and may wipe the repo, not my fault if it breaks the aurpm repo!
                  fs::copy("work/*/*.pkg.tar.zst",(val + &"/.aurpm/repo/".to_string())[..]);
                  println!("Finished Repo");
          
            }, 
            Err(e) => println!("couldn't interpret {}: {}", key, e),
        }
  }
}
