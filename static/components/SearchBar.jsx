import React from 'react'
import PropTypes from 'prop-types'

const SearchBar = props => (
  <div>
    <input type="text" />
    <button onClick={props.onClick}>
      Search
    </button>
  </div>
)

SearchBar.propTypes = {
  onClick: PropTypes.func.isRequired,
}

export default SearchBar
