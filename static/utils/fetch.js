import { analyzeUrl } from './urls'

const _fetch = (method, url, object) => {
  const config = {
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json',
    },
    method,
    body: JSON.stringify(object),
  }
  return fetch(url, config)
}

const _post = (url, object) => _fetch('POST', url, object)

export async function analyzePost(object)  {
  let response = await _post(analyzeUrl, object)
}
