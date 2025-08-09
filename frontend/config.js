import { ENV } from './env.js';

const BOT_CONFIG = {
  region: ENV.AWS_REGION,
  identityPoolId: ENV.COGNITO_IDENTITY_POOL_ID,
  botId: ENV.BOT_ID,
  botAliasId: ENV.BOT_ALIAS_ID,
  localeId: ENV.LOCALE_ID
};

export { BOT_CONFIG };