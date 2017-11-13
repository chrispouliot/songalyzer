import React from 'react'
import propTypes from 'prop-types'

const Duration = ({ hours, minutes }) => {
  let fmtHours = ''
  let fmtMinutes = ''

  if (hours) {
    fmtHours = `${hours}h`
  }
  if (minutes) {
    fmtMinutes = `${minutes}m`
  }

  return (
    <span>{`Duration: ${fmtHours} ${fmtMinutes}`}</span>
  )
}

Duration.propTypes = {
  hours: propTypes.number.isRequired,
  minutes: propTypes.number.isRequired,
}


export default Duration
