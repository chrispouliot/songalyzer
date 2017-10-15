import React, { Component } from 'react'
import PropTypes from 'prop-types'

class SearchBar extends Component {

  constructor() {
    super()
    this.handleClick = this.handleClick.bind(this)
    this.handleChange = this.handleChange.bind(this)
  }

  state = {
    input: '',
  }

  handleChange(evt) {
    console.log(evt)
    this.setState({
      input: evt.target.value,
    })
  }

  handleClick() {
    console.log("handleClick")
    console.log(this.state.input)
    this.props.onClick(this.state.input)
  }

  render() {
    return (
      <div>
        <input type="text" />
        <button
          value={this.state.input}
          onChange={this.handleChange}
          onClick={this.handleClick}
        >
          Search
        </button>
      </div>)
  }

}

SearchBar.propTypes = {
  onClick: PropTypes.func.isRequired,
}

export default SearchBar
