exports.handler = async (event) => {
  if (event.httpMethod !== 'POST') {
    return { statusCode: 405, body: 'Method Not Allowed' };
  }

  try {
    const res = await fetch('https://platform-api.max.ru/messages?user_id=3448828', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': process.env.MAX_BOT_TOKEN
      },
      body: event.body
    });

    const data = await res.text();

    return {
      statusCode: res.status,
      headers: {
        'Access-Control-Allow-Origin': '*',
        'Content-Type': 'application/json'
      },
      body: data
    };
  } catch (err) {
    return { statusCode: 502, body: JSON.stringify({ error: 'Proxy error' }) };
  }
};
