import React from 'react'

import SearchBar from './SearchBar'
import { SearchClick } from '../handlers'

const App = () => (
  <div>
    <SearchBar onClick={SearchClick} />
  </div>
)

export default App
