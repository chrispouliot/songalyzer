import React, { Component } from 'react'

import SearchBar from './SearchBar'
import { analyzePlaylist } from '.././utils/fetch'

class App extends Component {

  state = {}

  async searchClick(input) {
    const data = await analyzePlaylist(input)
    console.log(data)
  }

  render() {
    return (
      <div>
        <SearchBar onClick={this.searchClick} />
      </div>
    )
  }
}

export default App
