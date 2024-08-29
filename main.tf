# Copyright (c) HashiCorp, Inc.
# SPDX-License-Identifier: MPL-2.0

terraform {
  required_providers {
    spotify = {
      version = "~> 0.2.7"
      source  = "conradludgate/spotify"
    }
  }
}

provider "spotify" {
  api_key = var.spotify_api_key
}



resource "spotify_playlist" "playlist" {
  name        = "The Best of Ragga"
  description = "This playlist contains the best 20 hits of my RAGGA playlist. The playlist was created with Terraform."
  public      = true

  tracks = [
    "1WTuczRTn7aKpCPHxqsF9f", # Evil ways - Marcus Gad, Tribe
    "4uOKFydzAejjSFqYbv1XPt", # Red Red Wine - UB40
    "5O4erNlJ74PIF6kGol1ZrC", # Could You Be Loved - Bob Marley and The Wailers
    "3VJTOIVyeGujUIo6P0DoTx", # Le rendez vous - L'Entourloop
    "4JbMBbrm55qOW6lJwtKtfM" # Bob & Friends Over There - Ijahman Levi
  ]
}
