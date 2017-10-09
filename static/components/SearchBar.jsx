import React, { Component } from 'react'
import PropTypes from 'prop-types'

class SearchBar extends Component {

  static state = {
    input: '',
  }

  handleChange(evt) {
    this.setState({
      input: evt.target.value,
    })
  }

  handleClick() {
    this.props.onClick(this.state.input)
  }

  render() {
    return (
      <div>
        <input type="text" />
        <button
          value={this.state.input}
          onChange={evt => this.handleChange(evt)}
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
