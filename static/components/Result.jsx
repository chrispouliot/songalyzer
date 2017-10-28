import React, { Component } from 'react'
import PropTypes from 'prop-types'

export default class Result extends Component {
  render() {
    const playlist = this.props.playlist
    return (
      <div>
        <h2>{playlist.name} by {playlist.owner.id}</h2>
        <p>{playlist.description}</p>
        <ul>
          <li>Songs: {playlist.songs.length}</li>
          <li>Durarion: {playlist.duration}</li>
          <li>Average Popularity: {playlist.popularity}</li>
        </ul>
      </div>
    )
  }
}

// TODO: Object is of multiple types. Should look into addressing forbidden thing
Result.propTypes = {
  playlist: PropTypes.object.isRequired
}
