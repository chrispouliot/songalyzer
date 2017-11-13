import React from 'react'
import propTypes from 'prop-types'

const Error = ({ error }) => (error ? <div>{error}</div> : null)

Error.propTypes = {
  error: propTypes.string.isRequired,
}

export default Error
