import React, { Component } from 'react'
import PropTypes from 'prop-types'

import Duration from './Duration'
import Song from './Song'

import { format } from '../utils/duration'

const descriptionStyle = {
  minHeight: '1.2em',
}

const resultDivStyle = {
  display: 'inline-block',
  margin: '2em',
}

export default class Result extends Component {

  // TODO: Component for this?
  displayPopular() {
    const songs = this.props.playlist.songs
    if (songs.length > 1) {
      return (
        <div>
          <h3> Most Popular Song </h3>
          <Song song={songs.pop()} />
          <h3> Least Popular Song </h3>
          <Song song={songs.shift()} />
        </div>
      )
    }
    return <div />
  }

  render() {
    const playlist = this.props.playlist
    const duration = format(this.props.playlist.duration)

    return (
      <div style={resultDivStyle}>
        <h2>{playlist.name} by {playlist.owner.id}</h2>
        <p style={descriptionStyle}>{playlist.description}</p>
        <ul>
          <li>Songs: {playlist.songs.length}</li>
          <li><Duration hours={duration.hours} minutes={duration.minutes} /> </li>
          <li>Average Popularity: {playlist.popularity}</li>
        </ul>
        {this.displayPopular()}
      </div>
    )
  }
}

// TODO: Object is of multiple types. Should look into addressing forbidden thing
Result.propTypes = {
  playlist: PropTypes.object.isRequired,
}
