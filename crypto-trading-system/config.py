# ETH合约AI预测系统配置文件

import os

# 数据配置
DATA_CONFIG = {
    'symbol': 'ETH/USDT',           # 交易对
    'timeframes': ['1m', '5m', '15m', '1h', '4h'],  # 多时间框架
    'history_days': 90,             # 历史数据天数
    'update_interval': 60,          # 数据更新间隔(秒)
    'features': [                   # 特征列表
        'open', 'high', 'low', 'close', 'volume',
        'rsi', 'macd', 'bb_upper', 'bb_lower', 'ma_20', 'ma_50',
        'atr', 'obv', 'stoch_k', 'stoch_d', 'cci'
    ],
    'prediction_horizon': [5, 15, 30, 60],  # 预测时间(分钟)
    'data_source': 'binance',       # 数据源
}

# AI模型配置
MODEL_CONFIG = {
    'models': {
        'lstm': {
            'enabled': True,
            'sequence_length': 60,      # 输入序列长度
            'hidden_units': [128, 64],  # 隐藏层单元数
            'dropout': 0.2,
            'learning_rate': 0.001,
            'batch_size': 32,
            'epochs': 100,
        },
        'transformer': {
            'enabled': True,
            'sequence_length': 48,
            'num_heads': 8,
            'num_layers': 4,
            'dim_model': 128,
            'dropout': 0.1,
            'learning_rate': 0.0001,
            'batch_size': 16,
            'epochs': 50,
        },
        'cnn_lstm': {
            'enabled': True,
            'sequence_length': 30,
            'cnn_filters': [32, 64, 128],
            'kernel_size': 3,
            'lstm_units': 64,
            'dropout': 0.3,
            'learning_rate': 0.001,
            'batch_size': 32,
            'epochs': 80,
        }
    },
    'ensemble': {
        'enabled': True,            # 是否启用集成学习
        'weights': [0.4, 0.35, 0.25],  # 各模型权重
        'voting_method': 'weighted',    # 投票方法
    },
    'model_save_path': 'models/saved/',
    'auto_save': True,
    'validation_split': 0.2,
}

# 训练配置
TRAINING_CONFIG = {
    'auto_retrain': True,           # 自动重训练
    'retrain_interval': 24,         # 重训练间隔(小时)
    'min_accuracy_threshold': 0.65, # 最低准确率阈值
    'early_stopping': True,         # 早停
    'early_stopping_patience': 10,  # 早停耐心值
    'data_augmentation': True,      # 数据增强
    'cross_validation': True,       # 交叉验证
    'cv_folds': 5,                  # 交叉验证折数
    'hyperparameter_tuning': True,  # 超参数调优
    'tuning_trials': 50,            # 调优试验次数
}

# 预测配置
PREDICTION_CONFIG = {
    'confidence_threshold': 0.7,    # 置信度阈值
    'prediction_interval': 30,      # 预测间隔(秒)
    'trend_sensitivity': 0.002,     # 趋势敏感度(0.2%)
    'volatility_adjustment': True,  # 波动率调整
    'multi_timeframe': True,        # 多时间框架分析
    'signal_strength': {            # 信号强度分级
        'strong_buy': 0.8,
        'buy': 0.6,
        'hold': 0.4,
        'sell': 0.3,
        'strong_sell': 0.2,
    }
}

# 合约交易配置
CONTRACT_CONFIG = {
    'exchange': 'binance_futures',  # 期货交易所
    'api_key': '',                  # API密钥
    'secret': '',                   # 密钥
    'testnet': True,                # 测试网络
    'symbol': 'ETHUSDT',            # 合约交易对
    'leverage': 10,                 # 杠杆倍数
    'position_mode': 'hedge',       # 持仓模式(hedge/oneway)
    'margin_type': 'isolated',      # 保证金模式
    'order_types': ['market', 'limit', 'stop_market'],
    'max_position_size': 1000,      # 最大持仓(USDT)
    'min_order_size': 10,           # 最小订单(USDT)
}

# 风险管理配置
RISK_CONFIG = {
    'max_drawdown': 0.15,           # 最大回撤15%
    'position_sizing': 'kelly',     # 仓位计算方法
    'risk_per_trade': 0.02,         # 单笔风险2%
    'stop_loss': {
        'enabled': True,
        'atr_multiplier': 2.0,      # ATR倍数止损
        'max_loss_percent': 0.05,   # 最大损失5%
    },
    'take_profit': {
        'enabled': True,
        'risk_reward_ratio': 2.0,   # 风险收益比
        'trailing_stop': True,      # 移动止盈
    }
}

# GUI界面配置
GUI_CONFIG = {
    'language': 'zh_CN',            # 中文界面
    'theme': 'dark',                # 主题(dark/light)
    'window_size': (1400, 900),     # 窗口大小
    'update_frequency': 1000,       # 界面更新频率(毫秒)
    'charts': {
        'main_timeframe': '15m',    # 主图时间周期
        'indicators': ['MA20', 'MA50', 'RSI', 'MACD', 'Volume'],
        'prediction_display': True,  # 显示预测
        'confidence_display': True,  # 显示置信度
    },
    'alerts': {
        'sound_enabled': True,      # 声音提醒
        'popup_enabled': True,      # 弹窗提醒
        'wechat_notify': False,     # 微信通知
    }
}

# 日志配置
LOGGING_CONFIG = {
    'level': 'INFO',
    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    'file_path': 'logs/',
    'max_file_size': 10485760,      # 10MB
    'backup_count': 5,
    'console_output': True,
}

# 系统配置
SYSTEM_CONFIG = {
    'debug_mode': True,
    'performance_monitoring': True,
    'auto_backup': True,
    'backup_interval': 3600,        # 备份间隔(秒)
    'gpu_enabled': True,            # 启用GPU加速
    'cpu_cores': -1,                # CPU核心数(-1为全部)
    'memory_limit': 8192,           # 内存限制(MB)
}

# 验证配置
def validate_config():
    """验证配置有效性"""
    errors = []
    
    # 检查AI模型配置
    enabled_models = [name for name, config in MODEL_CONFIG['models'].items() if config['enabled']]
    if not enabled_models:
        errors.append("至少需要启用一个AI模型")
    
    # 检查数据配置
    if DATA_CONFIG['history_days'] < 30:
        errors.append("历史数据天数至少需要30天")
    
    # 检查风险配置
    if RISK_CONFIG['max_drawdown'] > 0.3:
        errors.append("最大回撤不应超过30%")
    
    # 检查合约配置
    if not SYSTEM_CONFIG['debug_mode'] and not CONTRACT_CONFIG['api_key']:
        errors.append("生产模式需要配置API密钥")
    
    return errors

# 获取配置
def get_config(section=None):
    """获取配置"""
    config_map = {
        'data': DATA_CONFIG,
        'model': MODEL_CONFIG,
        'training': TRAINING_CONFIG,
        'prediction': PREDICTION_CONFIG,
        'contract': CONTRACT_CONFIG,
        'risk': RISK_CONFIG,
        'gui': GUI_CONFIG,
        'logging': LOGGING_CONFIG,
        'system': SYSTEM_CONFIG,
    }
    
    if section is None:
        return config_map
    return config_map.get(section, {})

# 动态调整配置
def update_config(section, key, value):
    """动态更新配置"""
    config_map = get_config()
    if section in config_map and key in config_map[section]:
        config_map[section][key] = value
        return True
    return False

if __name__ == "__main__":
    # 验证配置
    errors = validate_config()
    if errors:
        print("❌ 配置错误:")
        for error in errors:
            print(f"  • {error}")
    else:
        print("✅ 配置验证通过")
        
    # 显示启用的模型
    enabled_models = [name for name, config in MODEL_CONFIG['models'].items() if config['enabled']]
    print(f"🤖 启用的AI模型: {', '.join(enabled_models)}")
    print(f"📊 预测时间框架: {DATA_CONFIG['prediction_horizon']} 分钟")
    print(f"⚡ GPU加速: {'启用' if SYSTEM_CONFIG['gpu_enabled'] else '禁用'}")