pub mod aur_use {
    use reqwest;
    use serde::Deserialize;    

    #[derive(Debug, Deserialize)]
    #[serde(rename_all = "camelCase")] 
    pub struct AurResponse {
        pub version: i16,
        pub r#type: String,
        pub resultcount: i32,
    }

    pub async fn does_pkg_exist(pkg_name: &str) -> Result<AurResponse, reqwest::Error> {
        let resp: AurResponse = reqwest::get(pkg_name)
        .await?
        .json::<AurResponse>()
        .await?;
        Ok(resp)
    }
}

