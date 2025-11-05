<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DALA Chat Database Architecture</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            background: #0a0e27;
            color: #e4e7eb;
            padding: 40px 20px;
            min-height: 100vh;
            line-height: 1.6;
        }
        
        .container {
            max-width: 1600px;
            margin: 0 auto;
        }
        
        header {
            text-align: center;
            margin-bottom: 60px;
            padding-bottom: 30px;
            border-bottom: 1px solid rgba(255,255,255,0.1);
        }
        
        h1 {
            font-size: 3em;
            font-weight: 700;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 15px;
            letter-spacing: -1px;
        }
        
        .subtitle {
            color: #9ca3af;
            font-size: 1.1em;
            font-weight: 300;
        }
        
        .stats {
            display: flex;
            justify-content: center;
            gap: 40px;
            margin-top: 30px;
            flex-wrap: wrap;
        }
        
        .stat-item {
            text-align: center;
        }
        
        .stat-number {
            font-size: 2.5em;
            font-weight: 700;
            background: linear-gradient(135deg, #667eea, #764ba2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        .stat-label {
            color: #9ca3af;
            font-size: 0.9em;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-top: 5px;
        }
        
        .section {
            margin-bottom: 60px;
        }
        
        .section-header {
            display: flex;
            align-items: center;
            gap: 15px;
            margin-bottom: 30px;
        }
        
        .section-title {
            font-size: 1.8em;
            font-weight: 600;
            color: #fff;
        }
        
        .section-badge {
            background: rgba(102, 126, 234, 0.2);
            color: #667eea;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.85em;
            font-weight: 500;
        }
        
        .tables-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(380px, 1fr));
            gap: 25px;
        }
        
        .table-card {
            background: linear-gradient(135deg, #1a1f3a 0%, #151929 100%);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 16px;
            overflow: hidden;
            transition: all 0.3s ease;
            position: relative;
        }
        
        .table-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: linear-gradient(90deg, #667eea, #764ba2);
            opacity: 0;
            transition: opacity 0.3s ease;
        }
        
        .table-card:hover {
            transform: translateY(-8px);
            box-shadow: 0 20px 40px rgba(102, 126, 234, 0.3);
            border-color: rgba(102, 126, 234, 0.5);
        }
        
        .table-card:hover::before {
            opacity: 1;
        }
        
        .table-header {
            padding: 25px;
            background: rgba(255,255,255,0.03);
            border-bottom: 1px solid rgba(255,255,255,0.1);
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        
        .table-name {
            font-size: 1.3em;
            font-weight: 600;
            color: #fff;
            display: flex;
            align-items: center;
            gap: 12px;
        }
        
        .table-icon {
            width: 40px;
            height: 40px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 10px;
            font-size: 1.2em;
        }
        
        .icon-user { background: linear-gradient(135deg, #10b981, #059669); }
        .icon-chat { background: linear-gradient(135deg, #3b82f6, #2563eb); }
        .icon-security { background: linear-gradient(135deg, #ef4444, #dc2626); }
        .icon-log { background: linear-gradient(135deg, #f59e0b, #d97706); }
        
        .table-badge {
            padding: 4px 12px;
            border-radius: 12px;
            font-size: 0.75em;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        .badge-core { background: rgba(16, 185, 129, 0.2); color: #10b981; }
        .badge-feature { background: rgba(59, 130, 246, 0.2); color: #3b82f6; }
        .badge-security { background: rgba(239, 68, 68, 0.2); color: #ef4444; }
        .badge-audit { background: rgba(245, 158, 11, 0.2); color: #f59e0b; }
        
        .table-body {
            padding: 20px 25px 25px;
        }
        
        .field {
            padding: 12px 15px;
            margin-bottom: 8px;
            background: rgba(255,255,255,0.03);
            border-radius: 8px;
            border-left: 3px solid transparent;
            transition: all 0.2s ease;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .field:hover {
            background: rgba(255,255,255,0.06);
            border-left-color: #667eea;
        }
        
        .field-left {
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .field-icon {
            opacity: 0.6;
            font-size: 1.1em;
        }
        
        .field-name {
            font-weight: 500;
            color: #e4e7eb;
            font-size: 0.95em;
        }
        
        .field-type {
            color: #9ca3af;
            font-size: 0.85em;
            font-family: 'Courier New', monospace;
            background: rgba(255,255,255,0.05);
            padding: 2px 8px;
            border-radius: 4px;
        }
        
        .primary-key {
            background: rgba(251, 191, 36, 0.1);
            border-left-color: #fbbf24;
        }
        
        .foreign-key {
            background: rgba(59, 130, 246, 0.1);
            border-left-color: #3b82f6;
        }
        
        .relationships {
            background: linear-gradient(135deg, #1a1f3a 0%, #151929 100%);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 16px;
            padding: 40px;
            margin-top: 40px;
        }
        
        .relationships h2 {
            font-size: 2em;
            margin-bottom: 30px;
            color: #fff;
            font-weight: 600;
        }
        
        .relationship-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 20px;
        }
        
        .relationship-card {
            background: rgba(255,255,255,0.03);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 12px;
            padding: 20px;
            transition: all 0.3s ease;
        }
        
        .relationship-card:hover {
            background: rgba(255,255,255,0.06);
            border-color: rgba(102, 126, 234, 0.5);
            transform: translateX(5px);
        }
        
        .relationship-card strong {
            color: #667eea;
            font-size: 1.05em;
            display: block;
            margin-bottom: 8px;
        }
        
        .relationship-card p {
            color: #9ca3af;
            font-size: 0.9em;
            line-height: 1.5;
        }
        
        .legend {
            display: flex;
            gap: 30px;
            justify-content: center;
            flex-wrap: wrap;
            padding: 25px;
            background: rgba(255,255,255,0.03);
            border-radius: 12px;
            margin-bottom: 40px;
        }
        
        .legend-item {
            display: flex;
            align-items: center;
            gap: 10px;
            color: #9ca3af;
            font-size: 0.9em;
        }
        
        .legend-box {
            width: 20px;
            height: 20px;
            border-radius: 4px;
        }
        
        .legend-pk { background: rgba(251, 191, 36, 0.3); border: 2px solid #fbbf24; }
        .legend-fk { background: rgba(59, 130, 246, 0.3); border: 2px solid #3b82f6; }
        
        @media (max-width: 768px) {
            h1 { font-size: 2em; }
            .tables-grid { grid-template-columns: 1fr; }
            .stats { gap: 20px; }
            .stat-number { font-size: 2em; }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>DALA Chat Database Architecture</h1>
            <p class="subtitle">Enterprise-Grade Messaging System Infrastructure</p>
            <div class="stats">
                <div class="stat-item">
                    <div class="stat-number">10</div>
                    <div class="stat-label">Tables</div>
                </div>
                <div class="stat-item">
                    <div class="stat-number">5</div>
                    <div class="stat-label">Security Layers</div>
                </div>
                <div class="stat-item">
                    <div class="stat-number">∞</div>
                    <div class="stat-label">Scalability</div>
                </div>
            </div>
        </header>
        
        <div class="legend">
            <div class="legend-item">
                <div class="legend-box legend-pk"></div>
                <span>Primary Key</span>
            </div>
            <div class="legend-item">
                <div class="legend-box legend-fk"></div>
                <span>Foreign Key</span>
            </div>
        </div>
        
        <!-- Core User Management -->
        <div class="section">
            <div class="section-header">
                <h2 class="section-title">Core User Management</h2>
                <span class="section-badge">2 Tables</span>
            </div>
            <div class="tables-grid">
                <div class="table-card">
                    <div class="table-header">
                        <div class="table-name">
                            <div class="table-icon icon-user">👤</div>
                            <span>Users</span>
                        </div>
                        <span class="table-badge badge-core">Core</span>
                    </div>
                    <div class="table-body">
                        <div class="field primary-key">
                            <div class="field-left">
                                <span class="field-icon">🔑</span>
                                <span class="field-name">user_id</span>
                            </div>
                            <span class="field-type">INT</span>
                        </div>
                        <div class="field">
                            <div class="field-left">
                                <span class="field-icon">📧</span>
                                <span class="field-name">email</span>
                            </div>
                            <span class="field-type">VARCHAR(255)</span>
                        </div>
                        <div class="field">
                            <div class="field-left">
                                <span class="field-icon">🔒</span>
                                <span class="field-name">password_hash</span>
                            </div>
                            <span class="field-type">VARCHAR(255)</span>
                        </div>
                        <div class="field">
                            <div class="field-left">
                                <span class="field-icon">👨</span>
                                <span class="field-name">username</span>
                            </div>
                            <span class="field-type">VARCHAR(100)</span>
                        </div>
                        <div class="field">
                            <div class="field-left">
                                <span class="field-icon">📝</span>
                                <span class="field-name">full_name</span>
                            </div>
                            <span class="field-type">VARCHAR(255)</span>
                        </div>
                        <div class="field">
                            <div class="field-left">
                                <span class="field-icon">📱</span>
                                <span class="field-name">phone_number</span>
                            </div>
                            <span class="field-type">VARCHAR(20)</span>
                        </div>
                        <div class="field">
                            <div class="field-left">
                                <span class="field-icon">🖼️</span>
                                <span class="field-name">profile_picture_url</span>
                            </div>
                            <span class="field-type">VARCHAR(500)</span>
                        </div>
                        <div class="field">
                            <div class="field-left">
                                <span class="field-icon">✅</span>
                                <span class="field-name">account_status</span>
                            </div>
                            <span class="field-type">ENUM</span>
                        </div>
                        <div class="field">
                            <div class="field-left">
                                <span class="field-icon">📅</span>
                                <span class="field-name">created_at</span>
                            </div>
                            <span class="field-type">TIMESTAMP</span>
                        </div>
                    </div>
                </div>
                
                <div class="table-card">
                    <div class="table-header">
                        <div class="table-name">
                            <div class="table-icon icon-security">🔐</div>
                            <span>User Sessions</span>
                        </div>
                        <span class="table-badge badge-security">Security</span>
                    </div>
                    <div class="table-body">
                        <div class="field primary-key">
                            <div class="field-left">
                                <span class="field-icon">🔑</span>
                                <span class="field-name">session_id</span>
                            </div>
                            <span class="field-type">INT</span>
                        </div>
                        <div class="field foreign-key">
                            <div class="field-left">
                                <span class="field-icon">🔗</span>
                                <span class="field-name">user_id</span>
                            </div>
                            <span class="field-type">INT</span>
                        </div>
                        <div class="field">
                            <div class="field-left">
                                <span class="field-icon">🎫</span>
                                <span class="field-name">session_token</span>
                            </div>
                            <span class="field-type">VARCHAR(255)</span>
                        </div>
                        <div class="field">
                            <div class="field-left">
                                <span class="field-icon">🌐</span>
                                <span class="field-name">ip_address</span>
                            </div>
                            <span class="field-type">VARCHAR(45)</span>
                        </div>
                        <div class="field">
                            <div class="field-left">
                                <span class="field-icon">💻</span>
                                <span class="field-name">user_agent</span>
                            </div>
                            <span class="field-type">VARCHAR(500)</span>
                        </div>
                        <div class="field">
                            <div class="field-left">
                                <span class="field-icon">⏰</span>
                                <span class="field-name">expires_at</span>
                            </div>
                            <span class="field-type">TIMESTAMP</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- Messaging System -->
        <div class="section">
            <div class="section-header">
                <h2 class="section-title">Messaging System</h2>
                <span class="section-badge">4 Tables</span>
            </div>
            <div class="tables-grid">
                <div class="table-card">
                    <div class="table-header">
                        <div class="table-name">
                            <div class="table-icon icon-chat">💬</div>
                            <span>Conversations</span>
                        </div>
                        <span class="table-badge badge-feature">Feature</span>
                    </div>
                    <div class="table-body">
                        <div class="field primary-key">
                            <div class="field-left">
                                <span class="field-icon">🔑</span>
                                <span class="field-name">conversation_id</span>
                            </div>
                            <span class="field-type">INT</span>
                        </div>
                        <div class="field">
                            <div class="field-left">
                                <span class="field-icon">📛</span>
                                <span class="field-name">conversation_name</span>
                            </div>
                            <span class="field-type">VARCHAR(255)</span>
                        </div>
                        <div class="field">
                            <div class="field-left">
                                <span class="field-icon">🔀</span>
                                <span class="field-name">conversation_type</span>
                            </div>
                            <span class="field-type">ENUM</span>
                        </div>
                        <div class="field foreign-key">
                            <div class="field-left">
                                <span class="field-icon">🔗</span>
                                <span class="field-name">created_by</span>
                            </div>
                            <span class="field-type">INT</span>
                        </div>
                        <div class="field">
                            <div class="field-left">
                                <span class="field-icon">📅</span>
                                <span class="field-name">created_at</span>
                            </div>
                            <span class="field-type">TIMESTAMP</span>
                        </div>
                    </div>
                </div>
                
                <div class="table-card">
                    <div class="table-header">
                        <div class="table-name">
                            <div class="table-icon icon-chat">💌</div>
                            <span>Messages</span>
                        </div>
                        <span class="table-badge badge-feature">Feature</span>
                    </div>
                    <div class="table-body">
                        <div class="field primary-key">
                            <div class="field-left">
                                <span class="field-icon">🔑</span>
                                <span class="field-name">message_id</span>
                            </div>
                            <span class="field-type">INT</span>
                        </div>
                        <div class="field foreign-key">
                            <div class="field-left">
                                <span class="field-icon">🔗</span>
                                <span class="field-name">conversation_id</span>
                            </div>
                            <span class="field-type">INT</span>
                        </div>
                        <div class="field foreign-key">
                            <div class="field-left">
                                <span class="field-icon">🔗</span>
                                <span class="field-name">sender_id</span>
                            </div>
                            <span class="field-type">INT</span>
                        </div>
                        <div class="field">
                            <div class="field-left">
                                <span class="field-icon">📝</span>
                                <span class="field-name">message_text</span>
                            </div>
                            <span class="field-type">TEXT</span>
                        </div>
                        <div class="field">
                            <div class="field-left">
                                <span class="field-icon">📎</span>
                                <span class="field-name">message_type</span>
                            </div>
                            <span class="field-type">ENUM</span>
                        </div>
                        <div class="field">
                            <div class="field-left">
                                <span class="field-icon">📂</span>
                                <span class="field-name">file_url</span>
                            </div>
                            <span class="field-type">VARCHAR(500)</span>
                        </div>
                    </div>
                </div>
                
                <div class="table-card">
                    <div class="table-header">
                        <div class="table-name">
                            <div class="table-icon icon-chat">👥</div>
                            <span>Participants</span>
                        </div>
                        <span class="table-badge badge-feature">Feature</span>
                    </div>
                    <div class="table-body">
                        <div class="field primary-key">
                            <div class="field-left">
                                <span class="field-icon">🔑</span>
                                <span class="field-name">participant_id</span>
                            </div>
                            <span class="field-type">INT</span>
                        </div>
                        <div class="field foreign-key">
                            <div class="field-left">
                                <span class="field-icon">🔗</span>
                                <span class="field-name">conversation_id</span>
                            </div>
                            <span class="field-type">INT</span>
                        </div>
                        <div class="field foreign-key">
                            <div class="field-left">
                                <span class="field-icon">🔗</span>
                                <span class="field-name">user_id</span>
                            </div>
                            <span class="field-type">INT</span>
                        </div>
                        <div class="field">
                            <div class="field-left">
                                <span class="field-icon">👑</span>
                                <span class="field-name">role</span>
                            </div>
                            <span class="field-type">ENUM</span>
                        </div>
                        <div class="field">
                            <div class="field-left">
                                <span class="field-icon">📅</span>
                                <span class="field-name">joined_at</span>
                            </div>
                            <span class="field-type">TIMESTAMP</span>
                        </div>
                    </div>
                </div>
                
                <div class="table-card">
                    <div class="table-header">
                        <div class="table-name">
                            <div class="table-icon icon-chat">✅</div>
                            <span>Message Receipts</span>
                        </div>
                        <span class="table-badge badge-feature">Feature</span>
                    </div>
                    <div class="table-body">
                        <div class="field primary-key">
                            <div class="field-left">
                                <span class="field-icon">🔑</span>
                                <span class="field-name">receipt_id</span>
                            </div>
                            <span class="field-type">INT</span>
                        </div>
                        <div class="field foreign-key">
                            <div class="field-left">
                                <span class="field-icon">🔗</span>
                                <span class="field-name">message_id</span>
                            </div>
                            <span class="field-type">INT</span>
                        </div>
                        <div class="field foreign-key">
                            <div class="field-left">
                                <span class="field-icon">🔗</span>
                                <span class="field-name">user_id</span>
                            </div>
                            <span class="field-type">INT</span>
                        </div>
                        <div class="field">
                            <div class="field-left">
                                <span class="field-icon">📅</span>
                                <span class="field-name">read_at</span>
                            </div>
                            <span class="field-type">TIMESTAMP</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- Security & Compliance -->
        <div class="section">
            <div class="section-header">
                <h2 class="section-title">Security & Compliance</h2>
                <span class="section-badge">4 Tables</span>
            </div>
            <div class="tables-grid">
                <div class="table-card">
                    <div class="table-header">
                        <div class="table-name">
                            <div class="table-icon icon-security">🚫</div>
                            <span>Blocked Users</span>
                        </div>
                        <span class="table-badge badge-security">Security</span>
                    </div>
                    <div class="table-body">
                        <div class="field primary-key">
                            <div class="field-left">
                                <span class="field-icon">🔑</span>
                                <span class="field-name">block_id</span>
                            </div>
                            <span class="field-type">INT</span>
                        </div>
                        <div class="field foreign-key">
                            <div class="field-left">
                                <span class="field-icon">🔗</span>
                                <span class="field-name">blocker_user_id</span>
                            </div>
                            <span class="field-type">INT</span>
                        </div>
                        <div class="field foreign-key">
                            <div class="field-left">
                                <span class="field-icon">🔗</span>
                                <span class="field-name">blocked_user_id</span>
                            </div>
                            <span class="field-type">INT</span>
                        </div>
                        <div class="field">
                            <div class="field-left">
                                <span class="field-icon">📝</span>
                                <span class="field-name">reason</span>
                            </div>
                            <span class="field-type">VARCHAR(500)</span>
                        </div>
                    </div>
                </div>
                
                <div class="table-card">
                    <div class="table-header">
                        <div class="table-name">
                            <div class="table-icon icon-security">🔍</div>
                            <span>Login Attempts</span>
                        </div>
                        <span class="table-badge badge-security">Security</span>
                    </div>
                    <div class="table-body">
                        <div class="field primary-key">
                            <div class="field-left">
                                <span class="field-icon">🔑</span>
                                <span class="field-name">attempt_id</span>
                            </div>
                            <span class="field-type">INT</span>
                        </div>
                        <div class="field">
                            <div class="field-left">
                                <span class="field-icon">📧</span>
                                <span class="field-name">email</span>
                            </div>
                            <span class="field-type">VARCHAR(255)</span>
                        </div>
                        <div class="field">
                            <div class="field-left">
                                <span class="field-icon">🌐</span>
                                <span class="field-name">ip_address</span>
                            </div>
                            <span class="field-type">VARCHAR(45)</span>
                        </div>
                        <div class="field">
                            <div class="field-left">
                                <span class="field-icon">✅</span>
                                <span class="field-name">success</span>
                            </div>
                            <span class="field-type">BOOLEAN</span>
                        </div>
                        <div class="field">
                            <div class="field-left">
                                <span class="field-icon">⏰</span>
                                <span class="field-name">attempt_time</span>
                            </div>
                            <span class="field-type">TIMESTAMP</span>
                        </div>
                    </div>
                </div>
                
                <div class="table-card">
                    <div class="table-header">
                        <div class="
