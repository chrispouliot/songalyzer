import { React, Component } from 'react'

import SearchBar from './SearchBar'
// import { SearchClick } from '../handlers'

class App extends Component {

  static state = {}

  searchClick = () => {

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
