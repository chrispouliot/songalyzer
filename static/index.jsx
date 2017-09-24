import React from 'react'
import { render } from 'react-dom'
import { HashRouter, Route, Switch } from 'react-router-dom'

import App from './components/App'
import NotFound from './components/NotFound'

const Routes = () => (
  <HashRouter>
    <Switch>
      <Route exact path="/" component={App} />
      <Route component={NotFound} />
    </Switch>
  </HashRouter>
)

render(<Routes />, document.getElementById('app'))

