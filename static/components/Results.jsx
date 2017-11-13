import React, { Component } from 'react'
import PropTypes from 'prop-types'

import Result from './Result'

export default class Results extends Component {

  renderLoading(loading) {
    return loading ? <div>Loading..</div> : <div />
  }

  render() {
    return (
      // TODO: Dont render based on name
      <div>
        {this.renderLoading(this.props.loading)}
        {this.props.playlists.map(playlist => <Result playlist={playlist} key={playlist.name} />)}
        <h2>Common songs</h2>
      </div>
    )
  }
}

Results.propTypes = {
  playlists: PropTypes.arrayOf(PropTypes.object).isRequired,
  loading: PropTypes.bool.isRequired,
}
