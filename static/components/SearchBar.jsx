import React, { Component } from 'react'
import PropTypes from 'prop-types'

const outerDivStyle = {
  display: 'table',
  margin: '0 auto',
}

const inputStyle = {
  padding: '10px',
  margin: '10px',
  height: '20px',
  width: '500px',
  border: '1px solid #eaeaea',
  outline: 'none',
  fontSize: '14px',
}

const buttonStyle = {
  borderRadius: '2px',
  background: '#ADD8E6',
  border: '1px solid #ADD8E6',
  color: '#FFFFFF',
  cursor: 'default',
  fontSize: '14px',
  fontWeight: 'bold',
  width: '100px',
  padding: '0 16px',
  height: '36px',
  textShadow: '0 0 2px #2f4f4f',
}

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
  }

  render() {
    return (
      <div style={outerDivStyle}>
        <input style={inputStyle} type="text" value={this.state.input} onChange={this.handleChange} />
        <button style={buttonStyle} onClick={() => this.props.onClick(this.state.input)}>
          Search
        </button>
      </div>)
  }

}

SearchBar.propTypes = {
  onClick: PropTypes.func.isRequired,
}

export default SearchBar
