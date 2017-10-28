import React, { Component } from 'react'
import PropTypes from 'prop-types'

import Result from './Result'

export default class Results extends Component {
  render() {
    return (
      // TODO: Dont render based on name
      <div>
        {this.props.playlists.map(playlist => <Result playlist={playlist} key={playlist.name} />)}
      </div>
    )
  }
}

Results.propTypes = {
  playlists: PropTypes.arrayOf(PropTypes.object).isRequired,
}
