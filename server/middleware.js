export function auth(req, res, next) {
  const authInfo = { login: process.env.BASIC_AUTH_USER, password: process.env.BASIC_AUTH_PASS };
  // parse login and password from headers
  const b64auth = (req.headers.authorization || '').split(' ')[1] || '';

  const [login, password] = Buffer.from(b64auth, 'base64').toString().split(':');

  // Verify login and password are set and correct
  if (login && password && login === authInfo.login && password === authInfo.password) {
    // Access granted...
    return next();
  }

  // Access denied...
  res.set('WWW-Authenticate', 'Basic realm="401"'); // change this
  res.status(401).send('Authentication required.'); // custom message
  return res;
}

export default {
  auth,
};
