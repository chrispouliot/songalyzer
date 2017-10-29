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
    this.setState({
      input: evt.target.value,
    })
  }

  handleClick() {
    this.props.onClick(this.state.input)
    this.props.setLoading()
  }

  render() {
    return (
      <div>
        <input type="text" value={this.state.input} onChange={this.handleChange} />
        <button onClick={this.handleClick}>
          Search
        </button>
      </div>)
  }

}

SearchBar.propTypes = {
  setLoading: PropTypes.func.isRequired,
  onClick: PropTypes.func.isRequired,
}

export default SearchBar
