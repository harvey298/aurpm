pub mod aurUse {
    use reqwest;
    use serde::Deserialize;    

    #[derive(Debug, Deserialize)]
    #[serde(rename_all = "camelCase")] 
    pub struct aurResponse {
        pub version: i16,
        pub r#type: String,
        pub resultcount: i32,
    }

    pub async fn DoesPkgExist(pkgName: &str) -> Result<aurResponse, reqwest::Error> { //Box<dyn std::error::Error>
        let resp: aurResponse = reqwest::get(pkgName)
        .await?
        .json::<aurResponse>()
        .await?;
        Ok(resp)
    }
}

