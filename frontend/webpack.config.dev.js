const path = require('path');
const webpack = require('webpack');

let API_HOST = 'localhost:8000';

module.exports = {
    devServer: {
        inline: true,
        host: '0.0.0.0',
        port: 3000,
        contentBase: './build'
    },
    entry: {
        app: './src/index.js'
    },
    module: {
        loaders: [
            {
                test: /\.(jpe?g|png|gif|svg)$/i,
<<<<<<< HEAD
                    loaders: [
                        'file-loader?hash=sha512&digest=hex&name=[hash].[ext]',
                        'image-webpack-loader?bypassOnDebug&optimizationLevel=7&interlaced=false'
                    ]
                },
=======
                loaders: [
                    'file-loader?hash=sha512&digest=hex&name=[hash].[ext]',
                    'image-webpack-loader?bypassOnDebug&optimizationLevel=7&interlaced=false'
                ]
            },
>>>>>>> 98b300a09056059e2d1b7008bdb550823968410a
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
                'API_ROOT': JSON.stringify(`http://${API_HOST}`)
            }
        })
    ]    
}