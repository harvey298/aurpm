mod aur_ask;
mod pkg_management;

extern crate serde_json;

use std::process::{Command};
use std::{env, thread};
use std::io::{stdout, Write};

use serde_json::{Result, Value, json};

use crate::aurUse::aurResponse;
use crate::aur_ask::aurUse;
use crate::pkg_management::pkgmanagement;

#[tokio::main]
async fn main() {
    let args: Vec<String> = env::args().collect();
    if args[1].contains("-S") {
        let pkg_name: &str = &args[2];
        println!("Searching for package named {}!",pkg_name);
        install_pkg(pkg_name).await;
    } else if args[1].contains("-H") {
        print_help_msg();
    } else {
        print_help_msg();
    }
}

async fn install_pkg(pkg_name: &str) {
    let aur_url: &str = "https://aur.archlinux.org/rpc/?v=5&type=search&arg=";

    let package_url_raw: String = aur_url.to_string() + pkg_name;
    let pkg_url: &str = &package_url_raw[..];

    let response: aurResponse = aurUse::DoesPkgExist(pkg_url).await.unwrap();
    if response.resultcount != 0 {
        println!("found Package named {}!",pkg_name);
        pkgmanagement::build(pkg_name.to_string());
    } else {
        println!("No Package named {} was found!",pkg_name);
    }
}

fn print_help_msg() {
    println!("----------------------------------------------------------------");
    println!("-S <pkgname>");
}