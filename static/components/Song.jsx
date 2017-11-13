import React, { Component } from 'react'
import propTypes from 'prop-types'

import Duration from './Duration'

import { format } from '../utils/duration'

export default class Song extends Component {
  render() {
    const song = this.props.song
    const duration = format(song.duration)
    return (
      <div>
        <p>{song.title} by {song.artist}</p>
        <p><Duration hours={duration.hours} minutes={duration.minutes} /> </p>
        <p>Popularity: {song.popularity}</p>
      </div>
    )
  }
}

Song.propTypes = {
  song: propTypes.object.isRequired,
}
