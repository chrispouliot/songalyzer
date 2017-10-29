import React, { Component } from 'react'

import SearchBar from './SearchBar'
import Results from './Results'
import { analyzePlaylist } from '.././utils/fetch'

class App extends Component {

  constructor() {
    super()
    this.state = {
      playlists: [],
      loading: false,
    }
    this.searchClick = this.searchClick.bind(this)
    this.setLoading = this.setLoading.bind(this)
  }

  setLoading() {
    this.setState({
      loading: true,
    })
  }

  async searchClick(input) {
    const data = await analyzePlaylist({ input })

    this.setState({
      playlists: data.playlists,
      loading: false,
    })
  }

  render() {
    return (
      <div>
        <SearchBar setLoading={this.setLoading} onClick={this.searchClick} />
        <Results loading={this.state.loading} playlists={this.state.playlists} />
      </div>
    )
  }
}

export default App
