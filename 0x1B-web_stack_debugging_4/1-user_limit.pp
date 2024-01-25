# 1-user_limit.pp

class user_limit {
  exec { 'set_file_limit':
    command => 'echo "holberton hard nofile 4096" >> /etc/security/limits.conf && echo "holberton soft nofile 4096" >> /etc/security/limits.conf',
    path    => ['/bin', '/sbin', '/usr/bin', '/usr/sbin'],
    onlyif  => 'test $(grep -c "holberton.*nofile" /etc/security/limits.conf) -eq 0',
  }

  exec { 'set_pam_limits':
    command => 'echo "session required pam_limits.so" >> /etc/pam.d/su',
    path    => ['/bin', '/sbin', '/usr/bin', '/usr/sbin'],
    onlyif  => 'test $(grep -c "pam_limits.so" /etc/pam.d/su) -eq 0',
  }
}

include user_limit
Enable the user holberton to login and open files without errors

# Increase hard file limit for holberton user
exec { 'increase-hard-file-limit-for-holberton-user':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf'
  path    => '/usr/local/bin/:/bin/'
}

#Increase soft file limit for user holberton
exec { 'increase-soft-file-limit-for-holberton-user':
  command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf'
  path    => '/usr/local/bin/:/bin/'
}
