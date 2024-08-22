# Create a Spotify Playlist with Terraform
I used Terraform data source to search Spotify tracks and use that data to build a playlist.

## Prerequisites
You will need:

- **Terraform:** version 1.0+
- **Docker**
- **Spotify account with developer access**


## Create Spotify developer app
Before you can use Terraform with Spotify, you need to create a Spotify developer app.

<div align="center">
    <img src="assets/images/spotify-dashboard.png" alt="Spotify Dashboard" />
</div>


Click on Create App and Fill out the name and the description according to your needs.

Once Spotify creates the app click on *Edit Settings*.

Copy the URI below into the *Redirect URI* field and click Add so that Spotify can find its authorization app on port 27228 at the correct path


```sh
http://localhost:27228/spotify_callback
```


<div align="center">
    <img src="assets/images/redirect-uri.png" alt="Redirect URI" />
</div>


## Run authorization server
Now that oyu created the Spotify app, we have to configure and start the athorization server proxy, which allows Terraform to interact with Spotify.

<div align="center">
    <img src="assets/images/proxy.png" alt="Athorization sever" />
</div>

In you terminal, you will need to set the redirect URI as an eviroment variable:

```sh
$ export SPOTIFY_CLIENT_REDIRECT_URI=http://localhost:27228/spotify_callback
```