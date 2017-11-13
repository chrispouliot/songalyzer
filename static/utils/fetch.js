import { analyzeUrl } from './urls'

// I cant believe fetch() doesn't accept an object for query params
const buildQueryParams = (object) => {
  const esc = encodeURIComponent
  return Object.keys(object)
      .map(k => `${esc(k)}=${esc(object[k])}`)
      .join('&')
}

async function _fetch(method, url, object) {
  const config = {
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json',
    },
    method,
  }
  switch (method) {
    case 'GET':
      url = `${url}?${buildQueryParams(object)}`
      break
    case 'POST':
      config.body = JSON.stringify(object)
      break
    default:
      console.log('what')
      return Promise.reject()
  }

  const response = await fetch(url, config)
  if (response.ok) return response.json()
  console.log(response)
  throw new Error(response.statusText)
}

export function analyze(playlists) {
  return _fetch('GET', analyzeUrl, playlists).then(resp => resp.json())
}
