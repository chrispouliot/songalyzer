import React, { Component } from 'react'

import SearchBar from './SearchBar'
import Results from './Results'
import { analyzePlaylist } from '.././utils/fetch'

class App extends Component {

  constructor() {
    super()
    this.state = {
      playlists: [],
    }
    this.searchClick = this.searchClick.bind(this)
  }

  async searchClick(input) {
    const data = await analyzePlaylist({ playlist_url: input })
    console.log(data)
    this.setState({
      playlists: data.playlists,
    })
  }

  render() {
    return (
      <div>
        <SearchBar onClick={this.searchClick} />
        <Results playlists={this.state.playlists} />
      </div>
    )
  }
}

export default App
