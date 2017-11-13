import React, { Component } from 'react'

import Error from './Error'
import SearchBar from './SearchBar'
import Results from './Results'
import { analyze } from '.././utils/fetch'

const outerAppStyle = {
  width: '100%',
}

const innerAppStyle = {
  display: 'table',
  margin: '0 auto',
}

class App extends Component {

  constructor() {
    super()
    this.state = {
      playlists: [],
      loading: false,
      error: '',
    }
    this.searchClick = this.searchClick.bind(this)
    this.setLoading = this.setLoading.bind(this)
  }

  setLoading(loading) {
    this.setState({
      loading,
    })
  }

  setError(error) {
    // Should this not set loading to false?
    // Should I force calling both setError and setLoading?
    // Currently does both since would result in 1 render vs 2
    this.setState({
      error,
      loading: false,
    })
  }

  async searchClick(input) {
    this.setLoading(true)
    if (!input) {
      this.setError('No playlists entered')
      return
    }

    try {
      const data = await analyze(input.split(', '))
      this.setState({
        playlists: data.playlists,
        loading: false,
      })
    } catch (e) {
      console.log("got error, message is:")
      console.log(e.message)
      this.setError(e.message)
    }
  }

  render() {
    return (
      <div style={outerAppStyle}>
        <div style={innerAppStyle}>
          <SearchBar onClick={this.searchClick} />
          <Error error={this.state.error} />
          <Results loading={this.state.loading} playlists={this.state.playlists} />
        </div>
      </div>
    )
  }
}

export default App
