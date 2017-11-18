const path = require('path');
const webpack = require('webpack');

let API_HOST = '';
if (process.env.NODE_ENV === 'production') API_HOST = 'api.darthvendor.me';

module.exports = {
    entry: {
        app: './src/index.js'
    },
    module: {
        loaders: [
            {
                test: /\.(jpe?g|png|gif|svg)$/i,
                loaders: [
                    'file-loader?hash=sha512&digest=hex&name=[hash].[ext]',
                    'image-webpack-loader?bypassOnDebug&optimizationLevel=7&interlaced=false'
                ]
            },
            {
                test: /\.js$/,
                loaders: ['babel-loader'],
                exclude: /node_modules/
            },
            {
                test: /\.scss$/,
                loaders: [
                    'style-loader', 'css-loader', 'sass-loader'
                ]
            },
            {
                test: /\.mp3$/,
                loader: 'file-loader'
             }
        ]
    },
    output: {
        path: path.join(__dirname, 'build'),
        filename: 'js/bundle.min.js'
    },
    plugins: [
        new webpack.DefinePlugin({
            'process.env': {
                'NODE_ENV': JSON.stringify('production'),
                'API_ROOT': JSON.stringify(`http://${API_HOST}`)
            }
        })
    ]    
}